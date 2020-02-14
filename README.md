# MTSpread  

Utilitário de linha de comando para operações de spread em commodities agrícolas com o MetaTrader 5.  

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
> spread <ativo1> <ativo2> [-c 250]  
``` 
Exibe dados do spread entre ativo1 e ativo2 em 250 períodos  
exemplo:  
```
> spread ccmk20 ccmh20
```

resultado:  

4.00  
media 3.97  
maxima 4.80  
minima 3.64  
desvio padrao 0.18  
