with open("Python/Team/hr_system.txt") as file:
    for line in file:
        line = line.strip()
        name, id_number, job_title, salary = line.split(",")
        # print(f"Name: {name}, Title: {job_title}")
        
        # Stretch Challenge
        # Number 1
        # print(f"{name} (ID: {id_number}), {job_title} - ${int(salary):.2f}")
        
        # Number 2
        pay_check = int(salary) / 2 / 12
        # print(f"{name} (ID: {id_number}), {job_title} - ${pay_check:.2f}")
        
        # Number 3
        if job_title == "Engineer":
            pay_check += 1000
            
        print(f"{name} (ID: {id_number}), {job_title} - ${pay_check:.2f}")