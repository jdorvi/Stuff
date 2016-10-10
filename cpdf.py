def cpdf(data, dstride, h, kernel, n, x, xstride, y):  
    
    if len(n) != 0:
      ndata = len(n)
    else:
      print('not enough data.')
      return
    #Epanechnikov
    factor = 0.25/ndata
    y = []
    for i in range(n):
      ordinate = x[i]      
      y.append(0)
      for j in range(ndata):
        u = (ordinate - data[j])/h
        if u < -1:
          pass
        elif u > 1:
          y[i] += 4
        else:
          y[i] += (-u*u*u+3*u+2)
    for i in range(n):
      y[i] = y[i]*factor



void cpdfc(int ndata, double data[], int dstride, double h, char kernel,
           int n, double x[], int xstride, double y[])
{ int i, j;
  switch (kernel)
  { case 'e': /* Epanechnikov */
    { const double factor = 0.25/ndata;
      for (i = 0; i < n; i++)
      { double ordinate = x[i*xstride];
        y[i] = 0.0;
        for (j = 0; j < ndata; j++)
        { double u = (ordinate - data[j*dstride]) / h;
          if (u > +1.0) continue;
          if (u < -1.0) y[i] += 4.0;
          else y[i] += (2+u*u*u-3*u);
        }
      }
      for (i = 0; i < n; i++) y[i] *= factor;
      return;
    }

void cpdf(int ndata, double data[], int dstride, double h, char kernel,
          int n, double x[], int xstride, double y[])
{ int i, j;
  switch (kernel)
  { case 'e': /* Epanechnikov */
    { const double factor = 0.25/ndata;
      for (i = 0; i < n; i++)
      { double ordinate = x[i*xstride];
        y[i] = 0.0;
        for (j = 0; j < ndata; j++)
        { double u = (ordinate - data[j*dstride]) / h;
          if (u < -1.0) continue;
          if (u > +1.0) y[i] += 4.0;
          else y[i] += (-u*u*u+3*u+2);
        }
      }
      for (i = 0; i < n; i++) y[i] *= factor;
      return;
    }



