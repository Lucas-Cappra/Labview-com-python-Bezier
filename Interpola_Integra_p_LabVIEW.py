def function(x,y,z):
    
    import numpy as np
    print(x,y,z)
    x,y,z = float(x), float(y), float(z)
    print(x,y,z)

    a = np.array([x,y,z])    
    
    integral = np.trapz([x,y,z])

    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.title('Numpy Array')
    plt.plot(a, 'b--', label = 'numpy array', linewidth=2.0)
    plt.legend(loc = 'upper left')
    # plt.savefig('C:\\Users\\chericks\\Desktop\\Python\\LabVIEW\\plot.jpeg')
    plt.savefig('C:\\Users\\USUARIO\\Documents\\vstudiocode\\labVIEW\\plot.jpeg')

    plt.close()
    
    import scipy.constants as sc
    speed_of_light = sc.c    
    return ('O resultado é: '+str(a)+ ', a integral é: '+str(integral))

function("1","2","3")