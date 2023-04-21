clear all;
close all;
clc;
A=1.8;
t1=4*pi;
t2=8*pi;
alfa=1;
DB = 20;
t=[0:(24*pi)/1000:24*pi];
################# Interrupcion ##############################################
xinterrupcion=A*(1-alfa*(((t-t1)>0)-((t-t2)>0))).*sin(t);
xruido=awgn(xinterrupcion,DB,'measured');
#energia1=(xinterrupcion*xinterrupcion')/length(xinterrupcion);
#ruido=xruido-xinterrupcion;
#energia2=(ruido*ruido')/length(ruido);
#plot(xruido);
#snr=sqrt(energia1/energia2)
#snrDB=20*log10(snr)
%hold on;
csvwrite('interrupcion.csv', xruido);

################# Sag ##############################################
alfa=0.2;
xsag=A*(1-alfa*(((t-t1)>0)-((t-t2)>0))).*sin(t);
xruido=awgn(xsag,DB,'measured');
##energia1=(xsag*xsag')/length(xsag);
##ruido=xruido-xsag;
##energia2=(ruido*ruido')/length(ruido);
##plot(xruido);
##snr=sqrt(energia1/energia2)
##snrDB=20*log10(snr)
csvwrite('sag.csv', xruido);

################# Swell ##############################################
alfa=0.8;
xswell=A*(1+alfa*(((t-t1)>0)-((t-t2)>0))).*sin(t);
xruido=awgn(xswell,DB,'measured');
##energia1=(xswell*xswell')/length(xswell);
##ruido=xruido-xswell;
##energia2=(ruido*ruido')/length(ruido);
##plot(xruido);
##snr=sqrt(energia1/energia2)
##snrDB=20*log10(snr)
csvwrite('swell.csv', xruido);

################# Armonicos ##############################################
alfa2=0.1;
xharmonics=A*((sin(t))+(alfa2*sin(20*t)));
xruido=awgn(xharmonics,DB,'measured');
##energia1=(xharmonics*xharmonics')/length(xharmonics);
##ruido=xruido-xharmonics;
##energia2=(ruido*ruido')/length(ruido);
##plot(xruido);
##snr=sqrt(energia1/energia2)
##snrDB=20*log10(snr)
csvwrite('armonicos.csv', xruido);

################# Flicker ##############################################
alfa=0.1;
beta=20;
xflicker=A*(1+alfa*sin(beta*t)).*sin(t);
xruido=awgn(xflicker,DB,'measured');
##energia1=(xflicker*xflicker')/length(xflicker);
##ruido=xruido-xflicker;
##energia2=(ruido*ruido')/length(ruido);
##plot(xruido);
##snr=sqrt(energia1/energia2)
##snrDB=20*log10(snr)
csvwrite('flicker.csv', xruido);

################# Transitorios ##############################################
t1=4*pi;
t2=5*pi;
alfa=0.8;
betha=5;
%xtransients=A*(sin(t)+alfa*(exp(-(t-t1)./0.004)).*(((t-t1)>0)-((t-t2)>0)).*(sin(300*t)));
xtransients=A*(sin(t)+alfa*sin(betha*t).*(exp(-(t-t1)/0.004)).*(((t-t1)>0)-((t-t2)>0)));
xruido=awgn(xtransients,DB,'measured');
#energia1=(xtransients*xtransients')/length(xtransients);
#ruido=xruido-xtransients;
#energia2=(ruido*ruido')/length(ruido);
#plot(xruido);
#snr=sqrt(energia1/energia2)
#snrDB=20*log10(snr)
csvwrite('transients.csv', xruido);