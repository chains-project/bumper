Here's the fixed version of the `between` method:

```java
@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return new Timestamp(super.between(from, to).getTime());
}

// Add the following lines after the 'between' method
import java.sql.Timestamp;

// ...

@SuppressWarnings("deprecation")
public DateAndTime betweenDates(Date from, Date to) {
    return (DateAndTime) super.between(from, to);
}

@Override
public Timestamp between(Date from, Date to) throws IllegalArgumentException {
    return new Timestamp(betweenDates(from, to).getTime());
}
```

The solution is to create a new helper method `betweenDates` that returns `DateAndTime` and then use this method to get the time in milliseconds and create a new `Timestamp` object.