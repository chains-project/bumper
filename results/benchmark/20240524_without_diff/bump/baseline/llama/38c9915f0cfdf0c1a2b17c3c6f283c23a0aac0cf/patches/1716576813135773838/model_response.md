```java
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

String text = "2022-01-01 00:00:00";
SimpleDateFormat format = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
Date date = format.parse(text);
```