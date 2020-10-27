CREATE TABLE `entries` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `concept` TEXT NOT NULL,
  `entry` TEXT NOT NULL,
  `date` INTEGER NOT NULL,
  `moodId` INTEGER NOT NULL,
  FOREIGN KEY(`moodId`) REFERENCES `moods`(`id`)
);

CREATE TABLE `moods` (
  `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  `label` TEXT NOT NULL
);

INSERT INTO `entries` VALUES (1, "1235", "123", 1598458543321, 1);
INSERT INTO `entries` VALUES (2, "abc", "123", 1598458548239, 2);
INSERT INTO `entries` VALUES (3, "Delete", "Now Deleting", 1598458559152, 1);
INSERT INTO `entries` VALUES (4, "Angry", "jlj", 1598557358781, 3);
INSERT INTO `entries` VALUES (5, "678", "Now Deleting", 1598557373697, 4);

INSERT INTO `moods` VALUES (null, "Happy");
INSERT INTO `moods` VALUES (null, "Sad");
INSERT INTO `moods` VALUES (null, "Angry");
INSERT INTO `moods` VALUES (null, "Ok");
