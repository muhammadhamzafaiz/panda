import pandas as pd
import matplotlib.pyplot as plt

# Data
visitors = [100, 200, 300, 400, 500, 450, 720, 120, 540, 320]
sales = [1125, 4400, 9000, 5000, 3400, 6000, 3300, 8000, 3400, 12000]

# Create a DataFrame
data = {'Visitors': visitors, 'Sales': sales}
df = pd.DataFrame(data)

# Display the DataFrame as a table
print(df)

# Plotting the graph
plt.figure(figsize=(10, 6))
plt.plot(df['Visitors'], df['Sales'], marker='o', linestyle='-', color='b')
plt.title('Visitor and Sales Data')
plt.xlabel('Number of Visitors')
plt.ylabel('Sales Amount')
plt.grid()
plt.xticks(df['Visitors'])  # Set x-ticks to the visitor values
plt.yticks(range(0, 13000, 1000))  # Set y-ticks for better readability
plt.show()