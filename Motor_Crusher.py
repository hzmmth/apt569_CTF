import logging
import time

# https://github.com/hzmmth/apt569/Motor_Crusher.py

logging.basicConfig(filename='Motor_Crusher.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(message)s')

def destroy_motor():
    # 
    logging.info("Motor_Crusher.py started: Injecting destructive commands to motor controller.")
    print(" Motor Crusher active! Engine is being disabled in 5 hours  ...")

    #
    for i in range(18000, 0, -1):
        print(f"Destroying in {i} seconds...")
        time.sleep(1)

    logging.info("Motor_Crusher.py: Engine throttle overridden to zero, engine disabled.")
    print("Engine destroyed successfully.")

if __name__ == "__main__":
    destroy_motor()

# https://github.com/hzmmth/apt569/Motor_Crusher.py

# https://github.com/hzmmth/apt569/Motor_Crusher.py
