import random

def generate_otp(length=5):
    if length <= 0:
        raise ValueError("OTP length must be positive.")
    otp = ''.join([str(random.randint(0,9)) for _ in range(length) ])
    return otp

if __name__ == "__main__":
    otp = generate_otp()
    print("Your OTP from myotpgenerator is: ", otp)