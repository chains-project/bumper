```java
private org.hamcrest.Matcher<java.lang.String> manifestPushed() {
    String expected = String.format("latest: digest: %s", this.image.digest());
    return new org.hamcrest.core.StringContains(false, expected);
}
```