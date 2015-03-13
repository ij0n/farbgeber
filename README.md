# farbgeber

Ein zentraler Farbgeber um der c-base einen farblich einheitlichen und harmonischen, trotzdem dynamisch wechselnden farbton zu verleihen.

Derzeit hat der Farbgeber noch keine MQTT-Anbindung, aber diese soll er in Kürze erhalten. Dann dient der Farbgeber als Sensor in unserem MQTT-Netzwerk und bietet ständig 6 Farbwerte an. Diese Farbwerte stehen in harmonischem Zusammenhang.

Dieses System soll als Angebot dienen für alle diejenigen, die LEDs an Bord verbauen und irgendwann vor der Frage stehen wie und in welcher Farbe die LEDs leuchten sollen. In vielen Fällen resultiert dies in schnellen Regenbogenfading und dem Regenbogensyndrom. Die Vision ist, dass für jede LED-Installation lediglich Blinkmuster und Leuchtpattern erzeugt werden, die Farben aber vom Farbgeber kommen.

Der Farbgeber ist ein Farb-Inklusionist und achtet darauf dass ALLE Farben des Regenbogens gleich oft und gleich lang dargestellt werden. Es werden für jede Sekunde in einer Stunde jeweils 6 Farben erzeugt. Davon sind 5 Farben sich sehr ähnlich und können z.b. für Verläufe oder Hintergründe mit Bewegung genutzt werden. Die 6. Farbe ist der Harmoniekontrast zur ersten Farbe und soll wenig und als hervorstehender Kontrast benutzt werden. Als Faustregel gilt: 90-100% der LEDs sollten in einer der 5 Basisvariationen leuchten und 0-10% in der Kontrastfarbe.


needs: python2

```pip install -r requirements.txt```
