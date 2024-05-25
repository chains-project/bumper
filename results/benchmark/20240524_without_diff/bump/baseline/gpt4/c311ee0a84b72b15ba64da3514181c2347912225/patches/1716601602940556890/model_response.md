```java
public void describeTo(Description description) {
    if (description != null && expectedString != null) {
        description.appendText(expectedString);
    }
}
```