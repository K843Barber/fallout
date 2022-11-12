import numpy as np

def hex_generator():
    N = 60
    logs = []
    for i in range(N):
        if 0 < np.random.rand(N)[0] <= 0.25:
            logs.append(f'0xF{np.random.choice(np.setdiff1d(range(600, 800),1))}')

        elif 0.25 < np.random.rand(N)[0] <= 0.5:
            if np.random.rand(N)[0] < 0.5:
                logs.append(f'0xF{np.random.choice(np.setdiff1d(range(60, 80),1))}C')
            else:
                logs.append(f'0xF{np.random.choice(np.setdiff1d(range(60, 80),1))}A')

        elif 0.5 < np.random.rand(N)[0] <=0.75:
            if np.random.rand(N)[0] < 0.5:
                logs.append(f'0xF{np.random.choice(np.setdiff1d(range(6, 8),1))}E{np.random.choice(np.setdiff1d(range(0, 10),1))}')
            else:
                logs.append(f'0xF{np.random.choice(np.setdiff1d(range(6, 8),1))}B{np.random.choice(np.setdiff1d(range(0, 10),1))}')        

        else:
                logs.append(f'0xF{np.random.choice(np.setdiff1d(range(6, 8),1))}D{np.random.choice(np.setdiff1d(range(0, 10),1))}')        
    return logs

