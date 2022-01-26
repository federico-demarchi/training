DROP TABLE IF EXISTS `todos`;

CREATE TABLE `todos` (
  `task_id` int NOT NULL,
  `type` varchar(15) DEFAULT NULL,
  `title` varchar(45) DEFAULT NULL,
  `deadline` datetime DEFAULT NULL,
  `status` tinyint DEFAULT NULL,
  `comment` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`task_id`)
);

INSERT INTO `todos` VALUES
    (1,'cleaning','wash-dishes','2021-01-08 10:00:00',0,'easy job'),
    (2,'cleaning','toilet','2021-01-08 10:00:00',0,'the floor is ugly'),
    (3,'studing','start the flask project','2021-01-08 10:00:00',0,'Should already have sarted'),
    (4,'studing','study python','2021-01-10 10:00:00',1,'should revise'),
    (5,'working','meeting with hr','2021-01-18 10:00:00',0,'be clean');