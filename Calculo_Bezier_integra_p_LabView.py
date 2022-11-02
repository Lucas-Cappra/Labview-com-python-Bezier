
def Curva_Bezier(CX1,CX2,CX3,CX4, CY1, CY2, CY3, CY4,):
    CX1,CX2,CX3,CX4, CY1,CY2,CY3,CY4 = float(CX1), float(CX2), float(CX3), float(CX4), float(CY1), float(CY2), float(CY3), float(CY4)  
    from cv2 import sqrt
    from Bezier import Bezier
    import numpy as np	

    t_points = np.arange(0, 1, 0.01) #................................. Creates an iterable list from 0 to 1.
    points1 = np.array([[CX1, CY1], [CX2, CY2], [CX3, CY3], [CX4, CY4]]) #.... Creates an array of coordinates.
    curve1 = Bezier.Curve(t_points, points1) #......................... Returns an array of coordinates.

    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.figure()
    plt.grid()
    plt.plot(
        curve1[:, 0],   # x-coordinates.
        curve1[:, 1],    # y-coordinates.
    )
    plt.plot(
        points1[:, 0],  # x-coordinates.
        points1[:, 1],  # y-coordinates.
        'ro:',           # Styling (red, circles, dotted).
        label = 'numpy array', linewidth=2.0
    )
    #plt.show()
    plt.legend(loc = 'upper left')
    plt.show()

    #=== Salva a imagem do plot, útil para visualizar no LabVIEW ===#
    plt.savefig('C:\\Users\\USUARIO\\Documents\\vstudiocode\\labVIEW\\Biblioteca_Bezier\\plotBezier.jpeg')
    plt.close()
    #=== Cálculo do comprimento da linha da Curva de Bezier ===#
    # def ComprimentoBezier(Px, Py):
    HipotenusaTotal = 0
    for i in range(0,99):
        dx = curve1[i+1,0] - curve1[i,0]
        dy = curve1[i+1,1] - curve1[i,1]
        HipotenusaNova = (sqrt(pow(abs(dx),2) + pow(abs(dy),2)))
        HipotenusaTotal = HipotenusaTotal + HipotenusaNova

    integra = np.trapz(curve1[:, 1], curve1[:, 0])

    HipotenusaTotal = HipotenusaTotal[0,0]
    return ('O valor do comprimento da Curva de Bezier é '+str(HipotenusaTotal)+'\nSua integral é '+str(integra))


# points1[0, ]*pow((1-t),3) + 3*points1[1, :]*pow((1-t),2)*t + 3*points1[2,:]*pow(t,2)*(1-t) + points1[3, :]*pow(t, 3),
# points1[:, 0]*pow((1-t),3) + 3*points1[:, 1]*pow((1-t),2)*t + 3*points1[:,2]*pow(t,2)*(1-t) + points1[:, 3]*pow(t, 3)