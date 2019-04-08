create database db_dogfriends;
use db_dogfriends;

create table tb_proprietario(
id_prop 		   int primary key auto_increment,
nome 	   		   varchar(100) not null,
telefone  		   varchar(15) not null,
email	           varchar(100) not null,
senha	           varchar(100) not null,
descricao          text,
foto               blob,
genero	           varchar(20) not null
);

create table tb_animal(
id_animal	   int primary key auto_increment,
nome	   	   varchar(50) not null,
genero	       char(20) not null,
faz_atividade  boolean not null,
porte    	   varchar(10) not null,
raca	       varchar(50) not null,
comportamento  text,
foto		   blob,
dt_nasc		   datetime,
med_avaliacao  float,
id_prop		   int not null,

constraint fk_id_prop foreign key(id_prop) references tb_proprietario(id_prop)
);

create table tb_dogwalker(
id				int primary key auto_increment,
nome			varchar(100) not null,
cpf   			varchar(11) not null,
foto  			blob,
telefone 		varchar(15) not null,
email  			varchar(100) not null,
senha  			varchar(100) not null,
descricao 		text not null,
genero			varchar(20) not null,
situacao		varchar(15),
med_avaliacao	float,
tamanho_camisa  varchar(5)
);

create table tb_endereco(
id		    int primary key not null,
logradouro varchar(100) not null,
complemento varchar(20),
numero	   varchar(5) not null,
bairro	   varchar(100) not null,
cidade	   varchar(100) not null,
estado	   varchar(2) not null,
cep		   varchar(10) not null
);

create table tb_caminhada(
id_caminhada 		int,
id_proprietario			    int,
id_dogwalker 		int,
id_dog				int,
dt_hr_caminhada		datetime,
valor				decimal,
status_caminhada	varchar(20),

constraint pk_id_caminhada primary key(id_caminhada, id_proprietario, id_dogwalker, id_dog, dt_hr_caminhada),
constraint fk_id_proprietario foreign key id_proprietario references tb_proprietario(id_proprietario),
constraint fk_id_dogwalker foreign key id_dogwalker references tb_dogwalker(id_dogwalker),
constraint fk_id_dog foreign key id_dog references tb_dog(id_dog),
);


