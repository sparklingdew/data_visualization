# Examples of data visualization using Python

## Spain/US trading evolution 

The data used in the following graph was extracted from [ICEX][1] and [Datacomex][2].

![imports_exports](images/imports_exports.png)

The graph condenses this information:
 * Percentage of Spain trade with US relative to the total foreing trade in Spain as a function of time (x and y axes)
 * Volume of money involved in the trade (circle size)
 * Proportion of import vs export (proportion of red and blue in the circles)

From the graph it is seen that the trading volume between US and Spain has increased with time. It must be pointed out that it is not corrected by inflation. Spain used to import more than it expoerted to the US. However, this changed through time and now exports and imports are balanced. From a Spanish point of view, the importance of trade with the US has been steadily increasing from an all-time low in 2005.

[1]:https://www.icex.es/icex/es/navegacion-principal/todos-nuestros-servicios/informacion-de-mercados/paises/navegacion-principal/el-pais/relaciones-bilaterales/index.html?idPais=US
[2]:https://datacomex.comercio.es/Data/Index


## Mechanical tests

Sensors are placed along a specimen and a loading-unloading cycle is applied. To visualize the deformation (strain) upon loading, the following plots are generated.

![strain_profile_vs_time](images/strain_profile_vs_time.png)

Load peaks (blue curve) mostly coincide with strain peaks (read zones). In the first part of the test, sensors failed quite greatly as seen by the white regions. Throught the test, some sensors got stuck in over-compressed or over-strecthed values as denoted by the red and blue horizontal lines.

The hysteresis curve during loading-unloading suffered two important anomalies, as shown in the following graph. First, the horizontal loop that occurs during the compression stage. Second, negative hysteresis (note that as time goes by the curve gets darker, and it is seen that the unloading curves tend to lie behind the loading curves) which does not make physical sense. 
