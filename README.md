# stay-focused

# Introduction
Stay focused is a simple project that helps the user to boost their productivity by organizing the work in a work-break cycle (just like in the pomodoro method). The user specifies the length of the work session and once the session is over, they specify the length of the break.
The software will notify the user whenever a work session or a break has finished. In the latter case, it will regularly prompt the user to go back to work.
**stay-focused** was written using Python 3.6.

# Compatibility
The project is, for the time being, supported only on **Linux** machines. Additionally, the machine needs to have **zenity** installed.

# Usage

## Installing dependencies

Simply run

    pip install -r requirements.txt

## Running the program

Run

    python start.py*
    
## Using the program

* Start a working session taking <minutes> minutes:
   
      work <minutes>

* Start a break taking <minutes> minutes:
  
      break <minutes>
 
* Display help:

      help
      
 * Exit:
 
       exit
       
