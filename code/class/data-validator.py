class DataValidator:
    def __init__(self):
        self.errors = []

    def validate_email(self,email):
        if "@" not in email:
            self.errors.append(f"Invalid Email : {email}")
            return False

        return True

    def validate_age(self,age):
        if age<0 or age > 150:
            self.errors.append(f"Invalid Age : {age}")
            return False

        return True

    def get_errors(self):
        return self.errors


# use the validator 
validator = DataValidator()

# Note : we don't pass self, just the email
validator.validate_age(age=200)
validator.validate_email(email="rajat.shahi")
validator.validate_email(email="rajat.shahi@x.com")
errors = validator.get_errors()

print("ERROR",*errors,sep="\n")