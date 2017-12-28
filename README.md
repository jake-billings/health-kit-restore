# health-kit-restore

This repository contains a tutorial and supporting material for importing health data from a possibly corrupted SQLite Apple HealthKit database. I hope it helps somebody in the same situation as me.

I only wrote the Python script to support a few data types. The rest, I was able to get because I was storing them in another app. I ended up losing my sleep data entirely because I couldn't figure out category data. If you need to restore more, you probably can. You just might have to modify the script.

## Introduction
I love being able to track every calorie I eat, every step I take, and every hour I sleep using Apple's HealthKit API. However, one day, I opened the app and all my data was gone. This was under iOS 10, and it seemed like there was no hope for the months of data I had logged. My Apple HealthKit database was corrupted, and my data was gone. There was no support online. Updating to iOS 11 did not help. THe Genius Bar did not help. This is what to do when you've lost all other hope of restoring your HealthKit data. It's not for the faint of heart, and you're not going to save everything. However, you can save some datasets if you're lucky.

## Tutorial
### Step 1: Make an Encrypted Backup of your iPhone
If I had done this, I wouldn't be here. However, Apple charges a lot of money for space on a Mac, and I thought everything I need synced to the cloud anyway. I was wrong. iOS does not sync your health data to the cloud until iOS 11. However, it's a key step to attempting to restore the corrupted database.

It's key that this backup be encrypted. Otherwise, it will not contain your private medical data.

This step can be completed using iTunes.

### Step 2: Open the Backup using a Third-party Tool
I used a trial of iExplorer. You can use anything. It'll ask for your encrypted backup password.

### Step 3: Clone your Health App SQLite Database
I found the SQLite files under `/Health/Health/*.sqlite`. You want `healthdb.sqlite` and `healthdb_secure.sqlite`. Copy these to your computer.

### Step 4: Repair your Broken Database
Maybe you're lucky and everything will work if you skip this step. The whole reason I had to do this is because my database got corrupted, so this is kind of the critical step.

It works by dumping everything you possibly can from the old db into a new db. Corrupted entries are ignored.

You need sqlite3 for it to work. Macs have it installed already I think.

Move your working directory to wherever your sqlite files are.

Run `echo '.dump'|sqlite3 healthdb_secure.sqlite|sqlite3 health_db_secure_repaired2.sqlite`

### Step 5: Open the SQLite file
I used "DB Browser for SQLite." You can use any program that can open and run sql commands on the SQLite database. The CLI would probably work just fine.

Open healthdb_secure.sqlite.

I ran into an issue where it asked for a password. I could recreate it consistently and didn't try, but I never encountered the issue if I opened `healthdb.sqlite` first and then opened healthdb_secure.sqlite. Not really sure if that had an effect.

### Step 6: Query the Data
The SQL files are included in `/sql` in this repository. `activity.sql` extracts a table that contains activity from the Apple Watch. `samples.sql` extracts the precious data that you're probably looking for.

I didn't write these commands. See the credits section.

DBBrowser for SQLite lets you run SQL commands on databases, so just copy and paste the commands over. Then, run them.

### Step 7: Export the data as CSV
DBBrowser for SQLite lets you export the result of a SQL command using the dropdown at the bottom.

### Step 8: Process the data
Even after the SQL query, the data isn't super useful. You could probably write a better SQL command, but I don't know how.

I used a data import app that requires each type of data to be in its own column.

I just wrote a Python script to process it again to fit that format. To use it,

1. Name your SQL files the same things I did, `samples_better.csv` and `health_activity_cache.csv`.
1. Place them in the same place I did, which is a folder called `data` in the root of this repository.
1. Set your working directory as the root of this repository
1. Execute the python script

Then, a file called samples_processed.csv will be created in `data`.

### Step 9: Import the data to your working phone
Maybe you should just buy a new phone. In any case, make sure it's a working phone before you do this.

I used Health Importer by Paradox Customs. It's pretty good at importing health data from CSV. It costs three dollars, but that's nothing if you've already gone through all this.

## Credits
Thanks to MATTIA EPIFANI for uploading your slides publically to sans.org. I copied his SQL commands and reverse-engineering of the data type IDs.

[See Mattia Epifani's Slides Here](https://www.sans.org/summit-archives/file/summit-archive-1492186541.pdf)