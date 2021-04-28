from sklearn.linear_model import LinearRegression

reg = LinearRegression()
x = x.reshape(-1, 1)
reg.fit(x, y)
reg.coef_
reg.intercept_
reg.score(x, y) * 100
pred = reg.predict(x)

plt.plot(y, label="actual")
plt.plot(reg.predict(x), label='predicted values')
plt.legend()
plt.show()

#polynomial regression
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=3)
xp = poly.fit_transform(x)
xp
xdf = pd.DataFrame(xp)
xdf
reg.fit(xdf, y)

