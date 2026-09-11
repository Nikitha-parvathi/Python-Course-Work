# Matplotlib & Data Visualization All in One Program

import matplotlib.pyplot as plt
import seaborn as sns


# -----------------------------
# 1. Line Plot
# -----------------------------

months = ["Jan","Feb","Mar","Apr","May"]
sales = [20000,25000,22000,30000,35000]

plt.figure(figsize=(6,4))

plt.plot(
    months,
    sales,
    color="blue",
    marker="o",
    linestyle="-",
    linewidth=2
)

plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)

plt.show()



# -----------------------------
# 2. Bar Chart
# -----------------------------

departments = ["CSE","ECE","EEE","MECH"]
students = [120,95,80,60]

plt.figure(figsize=(6,4))

plt.bar(
    departments,
    students,
    color="green",
    edgecolor="black"
)

plt.title("Department Strength")
plt.xlabel("Department")
plt.ylabel("Students")

plt.show()



# -----------------------------
# 3. Histogram
# -----------------------------

marks = [
45,56,67,78,89,
90,55,60,61,70,
72,85,92,68,73
]

plt.figure(figsize=(6,4))

plt.hist(
    marks,
    bins=5,
    color="orange",
    edgecolor="black"
)

plt.title("Student Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Students")

plt.show()



# -----------------------------
# 4. Scatter Plot
# -----------------------------

hours = [1,2,3,4,5,6,7,8]
marks = [30,40,50,60,70,80,90,95]


plt.figure(figsize=(6,4))

plt.scatter(
    hours,
    marks,
    s=100,
    color="red",
    marker="o"
)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()



# -----------------------------
# 5. Pie Chart
# -----------------------------

brands = [
    "Apple",
    "Samsung",
    "OnePlus",
    "Others"
]

share = [35,30,20,15]


plt.figure(figsize=(6,4))

plt.pie(
    share,
    labels=brands,
    autopct="%1.1f%%",
    startangle=90,
    shadow=True
)

plt.title("Mobile Market Share")

plt.show()



# -----------------------------
# 6. Box Plot
# -----------------------------

salary = [
25000,27000,30000,
32000,35000,38000,
40000,42000,70000
]


plt.figure(figsize=(6,4))

plt.boxplot(
    salary,
    showmeans=True
)

plt.title("Salary Distribution")

plt.show()



# -----------------------------
# 7. Area Chart
# -----------------------------

days = [1,2,3,4,5,6,7]

visitors = [
200,250,230,
280,300,320,350
]


plt.figure(figsize=(6,4))


plt.fill_between(
    days,
    visitors,
    alpha=0.5
)

plt.plot(
    days,
    visitors,
    linewidth=2
)

plt.title("Website Visitors")
plt.xlabel("Days")
plt.ylabel("Visitors")

plt.show()



# -----------------------------
# 8. Heatmap
# -----------------------------

data = [
[80,75,90],
[60,70,85],
[95,88,92]
]


plt.figure(figsize=(6,4))

sns.heatmap(
    data,
    annot=True,
    cmap="YlOrRd",
    linewidths=1
)

plt.title("Student Marks Heatmap")

plt.show()



# -----------------------------
# 9. Subplot Dashboard
# -----------------------------

months = ["Jan","Feb","Mar","Apr"]

sales = [20,25,30,35]

profit = [5,7,8,10]


plt.figure(figsize=(10,5))


# First Chart
plt.subplot(2,2,1)

plt.plot(
    months,
    sales,
    marker="o"
)

plt.title("Sales")



# Second Chart
plt.subplot(2,2,2)

plt.bar(
    months,
    profit
)

plt.title("Profit")



# Third Chart
plt.subplot(2,2,3)

plt.hist(
    marks,
    bins=5
)

plt.title("Marks")



# Fourth Chart
plt.subplot(2,2,4)

plt.scatter(
    hours,
    marks
)

plt.title("Study vs Marks")



plt.suptitle("Business Analytics Dashboard")

plt.tight_layout()

plt.show()