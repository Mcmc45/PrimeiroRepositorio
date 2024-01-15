/* Lógico_3: */

CREATE TABLE cliente (
    id_cliente INTEGER(4) PRIMARY KEY,
    nome_cliente VARCHAR(80),
    idade_cliente INTEGER(2),
    cpf_cliente VACHAR(14),
    email_cliente VACHAR(30),
    sexo_cliente CHARACTER(1),
    carro INTEGER(4)
);

CREATE TABLE Entidade_1 (
);

CREATE TABLE carro (
    id_carro INTEGER(4) PRIMARY KEY,
    marca VARCHAR(20),
    modelo VARCHAR(10),
    motor VACHAR(10),
    cor VACHAR(20),
    acessorios VACHAR(30)
);
 
ALTER TABLE cliente ADD CONSTRAINT FK_cliente_2
    FOREIGN KEY (carro???)
    REFERENCES ??? (???);