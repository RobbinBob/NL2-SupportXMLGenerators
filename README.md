# NL2-SupportXMLGenerators
Some handy generators which make use of the support xml import for nl2 

## How to use
1. First download the zip file and extract it somewhere where you will remember it
2. Run the 'gradientsupport.py', a dialogue box should appear
3. Follow the instructions in the box and customise any of the parameters
4. Once it is complete it will generate a file 'gradient.xml'
5. Now you can import it into NoLimits2 using the support xml import option

## Tips and tricks
A handy tip is that you do not need to fill out each input, If you just leave them blank they will use default values, making it easier to debug different support setups!
  > ## List of all default values
  > * Type = Gradient line or 0
  > * Color 1 = black
  > * Color 2 = white
  > * Support Diameter = 0.5m
  > * Position 1 = '0 2 0' just above default ground height
  > * Position 2 = '0 7 0' 5m above position1

### *Some things to note*
She is a bit temperamental, it does require formating certain inputs in a certain order, for example;
  > When inputting xyz/rgb each needs to be separated by a space, '10 50 2' is ok, '10,50,2' or '10502' is not ok!
