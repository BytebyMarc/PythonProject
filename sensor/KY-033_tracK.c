#include <linux/init.h>
#include <linux/module.h>
#include <linux/device.h>
#include <linux/kernel.h>
#include <linux/gpio.h>
#include <linux/fs.h>
#include <asm/uaccess.h>

#define DEVICE_NAME "TracK"
#define CLASS_NAME "KY"


MODULE_LICENSE ("GPL");
MODULE_AUTHOR ("-RAFIQ-");
MODULE_DESCRIPTION ("KY-033 Tracking Sensor for RPI");
MODULE_VERSION ("0.1");

static int majorNumber;
static int inf_Status = 0;
int cp_cnt;
static struct class *cl = NULL;
static struct device *dev = NULL;

static unsigned int gpioTrck = 2;

static int open_init (struct inode *inodep, struct file *filep);
static ssize_t read_init (struct file *filep, char __user *buffer, size_t len, loff_t *offset);
static int release_init (struct inode *inodep, struct file *filep);

static struct file_operations fops = 
{
        .open = open_init,
        .read = read_init,
        .release = release_init,
};


static int __init ky033_init (void){

	printk(KERN_INFO "KY033: Initializing driver to KY-033 tracking sensor\n");

        majorNumber = register_chrdev (0, "TracK", &fops);

        if (majorNumber < 0){
                        printk (KERN_INFO "Failed to register ky033 device file\n");
                        return -EIO;
        }

        printk (KERN_INFO "KY033: Sensor TracK registered correctly with majorNumber = %d\n", majorNumber);

	cl = class_create (THIS_MODULE, CLASS_NAME);		// class_create (THIS_MODULE, "CLASS_NAME"); // ISO C90: NO mixing in declaration 

    if (IS_ERR(cl)){

        unregister_chrdev(majorNumber, DEVICE_NAME);
        printk(KERN_ALERT "Failed to register device CLASS\n");
        return -EIO;

        }

    dev = device_create (cl, NULL, MKDEV(majorNumber, 0), NULL, DEVICE_NAME);			// device_create (CLASS, NULL, MKDEV(MajNum, 0), NULL, "DEVICE_NAME")

	if (IS_ERR(dev)){

        class_destroy (cl);
        unregister_chrdev(majorNumber, DEVICE_NAME);
        printk(KERN_ALERT "Failed to register device CLASS\n");
        return -EIO;
        }


	if(!gpio_is_valid (gpioTrck)){
		printk (KERN_INFO "GPIO_ERR: Invalid GPIO PIN\n");
		return -ENODEV;
	}

	gpio_request (gpioTrck, "sysfs");				//     	int gpio_request(unsigned int gpio, const char *label)
	gpio_direction_input (gpioTrck);				//		int gpio_direction_input(unsigned int gpio)
	gpio_export (gpioTrck, false);					//      int gpio_export(unsigned int gpio, bool direction_may_change);



//	printk (KERN_INFO "KY033: Sensor chrDEV registered correctly\n");

	return 0;
}

static int open_init (struct inode *inodep, struct file *filep){

	printk (KERN_INFO "KY033: Device for sensor Opened\n");
	return 0;

}

static ssize_t read_init (struct file *filep, char __user *buffer, size_t len, loff_t *offset){

//    static int inf_Status = 0;

    inf_Status = gpio_get_value (gpioTrck);						//     int gpio_get_value(unsigned int gpio);

    cp_cnt = copy_to_user (buffer, &inf_Status, sizeof(inf_Status));

    if(cp_cnt == 0){

        printk (KERN_INFO "Something written to USER_SPACE\n");
        return 0;
    }

    else{
        printk (KERN_INFO "Failed to data transfer from space->(KERN 2 USER)\n");
        return -EFAULT;
    }

}

static int release_init (struct inode *inodep, struct file *filep){

	printk (KERN_INFO "KY033: Sensor Device closing\n");
	return 0;
}

static void __exit ky033_exit(void){

    device_destroy (cl, MKDEV(majorNumber, 0));
    class_unregister(cl);
    class_destroy (cl);
    unregister_chrdev(majorNumber, DEVICE_NAME);
    printk (KERN_INFO "Clearing the tracking sensor driver\n");

}

module_init (ky033_init);
module_exit (ky033_exit);
