# MTSpread  

Utilitário de linha de comando para operações de spread utilizando o MetaTrader 5.  

------------

## Pré-requisitos  

* [MetaTrader5](https://www.metatrader5.com/pt) - Plataforma de trading.  
* [API.ex5](https://drive.google.com/file/d/1Osofc0PfxHpKk6FVCVucaSGnlmSPtnaL/view?usp=sharing) - Expert advisor executando no MetaTrader5.  
* [Python](https://www.python.org/) - Interpretador de comandos disponível no prompt de comando.  


## Instalação

```
> pip install mtspread
```

## Comandos

spread - Retorna dados do spread entre 2 ativos.  
```
> spread <ativo1> <ativo2>  
``` 
Exibe dados do spread entre ativo1 e ativo2  
exemplo:  
```
> spread ccmk20 ccmh20
```

resultado:  

3.04  
media 2.87  
maxima 3.65  
minima 1.99  
desvio padrao 0.32  
