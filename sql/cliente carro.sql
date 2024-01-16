/* L�gico_3: */

CREATE TABLE cliente (
    id_cliente INTEGER(4) PRIMARY KEY,
    nome_cliente VARCHAR(80),
    idade_cliente INTEGER(2),
    sexo_cliente CHARACTER(1),
    cpf_cliente VARCHAR(14),
    email_cliente VARCHAR(30),
    carro INTEGER(4)
);

CREATE TABLE Entidade_1 (
);

CREATE TABLE carro (
    id_carro INTEGER(4) PRIMARY KEY,
    marca VARCHAR(20),
    modelo VARCHAR(10),
    motor VARCHAR(10),
    cor VARCHAR(20),
    acessorios VARCHAR(30)
);
 
ALTER TABLE cliente ADD CONSTRAINT FK_cliente_2
    FOREIGN KEY (carro)
    REFERENCES carro(id_carro);