create database db_dogfriends;
use db_dogfriends;

create table tb_dono(
id_dono 		   int primary key auto_increment,
nome_dono 	   varchar(100) not null,
telefone_dono  varchar(15) not null,
email_dono	   varchar(100) not null,
senha_dono	   varchar(100) not null,
descricao_dono  text,
logradouro varchar(100) not null,
numero	   varchar(5) not null,
bairro	   varchar(100) not null,
cidade	   varchar(100) not null,
estado	   varchar(2) not null,
cep		   varchar(10) not null,
foto_dono  text
);

create table tb_cachorro(
id_dog		   int primary key auto_increment,
nome_dog	   varchar(50) not null,
sexo_dog	   char(1) not null,
faz_atividade  boolean not null,
porte_dog	   varchar(10) not null,
raca_dog	   varchar(50) not null,
comportamento  text,
foto		   text,
id_dono		   int not null,

constraint fk_id_dono foreign key(id_dono) references tb_dono(id_dono)
);

create table tb_dogwalker(
id_dogwalker	int primary key auto_increment,
nome_dogwalker	varchar(100) not null,
cpf_dogwalker   varchar(11) not null,
foto_dogwalker  text,
telefone_dogwalker varchar(15) not null,
email_dogwalker  varchar(100) not null,
senha_dogwalker  varchar(100) not null,
descricao_dogwalker text,
logradouro varchar(100) not null,
numero	   varchar(5) not null,
bairro	   varchar(100) not null,
cidade	   varchar(100) not null,
estado	   varchar(2) not null,
cep		   varchar(10) not null
);

create table tb_caminhada(
id_caminhada 		int,
id_dono			    int,
id_dogwalker 		int,
id_dog				int,
dt_hr_caminhada		datetime,
valor				decimal,
status_caminhada	varchar(20),

constraint pk_id_caminhada primary key(id_caminhada, id_dono, id_dogwalker, id_dog, dt_hr_caminhada),
constraint fk_id_dono foreign key id_dono references tb_dono(id_dono),
constraint fk_id_dogwalker foreign key id_dogwalker references tb_dogwalker(id_dogwalker),
constraint fk_id_dog foreign key id_dog references tb_dog(id_dog),
);