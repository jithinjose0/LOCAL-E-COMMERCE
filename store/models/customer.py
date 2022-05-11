from djongo import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField (max_length=50)
    phone = models.CharField(max_length=10) 
    pincode = models.IntegerField(blank=True,null=True)
    email=models.EmailField()
    password = models.CharField(max_length=100)

    #to save the data
    def register(self):
        self.save()


    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email= email)
        except:
            return False
    @staticmethod
    def get_customer_by_id(id):
        return Customer.objects.get(id=id)


    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False

