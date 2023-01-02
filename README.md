# POS_System 

Aplicação para gerênciamento e controle de vendas.

### Status: Developing ⚠️ 

[![NPM](https://img.shields.io/npm/l/react)](https://github.com/MathBM/App.ManagerStock/blob/master/LICENSE)

## Sobre o Projeto
POS_System é uma aplicação Monolítica Desenvolvida em Kivy e Python para praticar programação.

A aplicação consiste em um sistema POS (Point of Sale), em que há é segregado em duas partes a do administrador e operador. Há a possibilidade de gerênciar usuários e produtos por parte do administrador, possui a frente de caixa para um operador poder utilizar na venda de produtos que foram préviamente cadastrados.

Há a possibilidade de empacotar a aplicação para qualquer tipo de sistema devido a versatilidade do Kivy.

# Tecnologias Utilizadas:

## Front-End
  <div>
    <img src="https://kivy.org/static/images/logo_kivy_white.png" width=5%>
    <h4> Kivy </h4>
  </div>

## Back-End
  <div>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"> 
  </div>

## More
  <div>
   <img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white">
   <img src="https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white">
  </div>
  
## How to Run

  1º Clone Repo
```bash
git clone https://github.com/MathBM/POS_System.git
```
  2ª Change to directory of Project
```bash 
cd ~/POS_System
```
  3º Creates Data dir
```bash
mkdir Data
```
  4º Install dependes of requeriments.txt
```bash
pip install requeriments.txt
```
  5º Run Docker Compose
```bash
docker-compose up
```
  6º Run main archive
```bash
python main.py
```

### Images

#### Login Screen
<img src="https://github.com/MathBM/POS_System/blob/master/assets/Login_Screen.png">

### Admin Screen
<img src="https://github.com/MathBM/POS_System/blob/master/assets/Admin_Screen_Logins.png">

## Operator Screen
<img src="https://github.com/MathBM/POS_System/blob/master/assets/Operator_Screen_Sale.png">
