create database db_dogfriends;
use db_dogfriends;

create table tb_proprietario(
id	   			   int primary key auto_increment,
nome 	   		   varchar(100) not null,
telefone  		   varchar(15) not null,
email	           varchar(100) not null,
senha	           varchar(100) not null,
descricao          text,
foto               blob,
genero	           varchar(20) not null
);

create table tb_animal(
id      	   int primary key auto_increment,
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

constraint fk_id_prop foreign key(id_prop) references tb_proprietario(id)
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

create table tb_conta_bancaria(
banco			varchar(100) not null,
agencia			varchar(10) not null,
conta			varchar(10) not null,
id_dogwalker	int not null,

constraint pk_conta_bancaria primary key(banco, agencia, conta),
constraint fk_id_dogwalker foreign key (id_dogwalker) references tb_dogwalker(id)
);


create table tb_endereco(
id		   int primary key auto_increment,
logradouro varchar(100) not null,
complemento varchar(20),
numero	   varchar(5) not null,
bairro	   varchar(100) not null,
cidade	   varchar(100) not null,
estado	   varchar(15) not null,
cep		   varchar(10) not null
);

create table tb_endereco_dogwalker(
id_endereco 	int,
id_dogwalker 	int,

constraint pk_endereco_dogwalker primary key(id_endereco, id_dogwalker),
constraint fk_id_dogwalker foreign key (id_dogwalker) references tb_dogwalker(id),
constraint fk_id_endereco foreign key (id_endereco) references tb_endereco(id)
);

insert into tb_endereco_dogwalker(id_endereco, id_dogwalker) values(2, 2);


create table tb_endereco_proprietario(
id_endereco 	int,
id_prop 	int,

constraint pk_endereco_propietario primary key(id_endereco, id_dogwalker),
constraint fk_id_proprietario foreign key (id_prop) references tb_proprietario(id),
constraint fk_id_endereco foreign key (id_endereco) references tb_endereco(id)
);

create table tb_caminhada(
id 							int auto_increment,
id_prop						int,
id_dogwalker 				int,
id_animal					int,
dt_hr_caminhada				datetime,
valor						decimal,
tempo_solicitado			datetime,
status_caminhada			varchar(20),
avaliacao_animal			int,
desc_avaliacao_animal		varchar(100),
avaliacao_dogwalker			int,
desc_avaliacao_dogwalker	varchar(100),
latitude_dogwalker			varchar(50),
longitude_dogwalker			varchar(50),
id_endereco_busca			int,

constraint pk_id_caminhada primary key(id_, id_prop, id_dogwalker, id_animal, dt_hr_caminhada),
constraint fk_id_proprietario foreign key (id_proprietario) references tb_proprietario(id),
constraint fk_id_dogwalker foreign key (id_dogwalker) references tb_dogwalker(id),
constraint fk_id_animal foreign key (id_animal )references tb_animal(id),
constraint fk_id_endereco foreign key (id_endereco_busca) references tb_endereco(id)
);

create table tb_cobranca(
id					int auto_increment,
id_caminhada		int,
valor				decimal,
cod_barras			varchar(100),
status_cobranca		varchar(50),
id_prop				int,
dt_vencimento		datetime,
dt_pagamento		datetime,

constraint pk_cobranca primary key(id, id_caminhada),
constraint fk_id_caminhada foreign key (id_caminhada) references tb_caminhada(id),
constraint fk_id_proprietario foreign key (id_prop) references tb_caminhada(id_prop)
);

create table tb_fotos_caminhada(
id_caminhada 	int,
dt_hr_foto		datetime,
foto			blob,

constraint pk_fotos_caminhada primary key(id_caminhada, dt_hr_foto),
constraint fk_id_caminhada foreign key (id_caminhada) references tb_caminhada(id)
);




