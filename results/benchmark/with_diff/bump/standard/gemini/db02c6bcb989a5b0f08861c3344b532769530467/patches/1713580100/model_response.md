```java
private static org.hamcrest.Matcher<java.lang.String> imagePulled(final java.lang.String image) {
    String message = String.format("Status: Downloaded newer image for %s", image);
    return new org.hamcrest.core.StringContains(message); // ++ new constructor that accepts only String
}
``` 
