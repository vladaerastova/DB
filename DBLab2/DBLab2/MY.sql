SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`person`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`person` (
  `id` INT NOT NULL,
  `PIB` VARCHAR(45) NULL,
  `personcol` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`car`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`car` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  `motor` VARCHAR(45) NULL,
  `cost` DOUBLE NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`rent`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`rent` (
  `id` INT NOT NULL,
  `person_id` INT NOT NULL,
  `car_id` INT NOT NULL,
  `date_take` DATE NULL,
  `date_back` VARCHAR(45) NULL,
  PRIMARY KEY (`id`, `person_id`, `car_id`),
  INDEX `fk_rent_person_idx` (`person_id` ASC),
  INDEX `fk_rent_car1_idx` (`car_id` ASC),
  CONSTRAINT `fk_rent_person`
    FOREIGN KEY (`person_id`)
    REFERENCES `mydb`.`person` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_rent_car1`
    FOREIGN KEY (`car_id`)
    REFERENCES `mydb`.`car` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
