CREATE DATABASE ralph;
CREATE USER 'ralph'@'localhost' IDENTIFIED BY 'panda';
GRANT ALL ON ralph.* TO 'ralph'@'localhost';

USE ralph;

CREATE TABLE Player (
	Player_id int PRIMARY KEY AUTO_INCREMENT,
	Username varchar (50) NOT NULL ,
	Password varchar (50) NOT NULL ,
	x float NULL ,
	y float NULL ,
	z float NULL ,
	rotation float NULL
);

INSERT INTO `player` (`username`, `password`) VALUES ('Test', '1234');