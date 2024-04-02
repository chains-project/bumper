```java
private Matcher<String> manifestPushed() {
    String expected = String.format("latest: digest: %s", this.image.digest());
    return new StringContains(expected);
}
```