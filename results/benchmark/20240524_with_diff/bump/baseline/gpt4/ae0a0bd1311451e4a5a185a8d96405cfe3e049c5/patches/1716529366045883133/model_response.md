```java
private Matcher<String> manifestPushed() {
    String formattedString = String.format("latest: digest: %s", this.image.digest());
    return new StringContains(formattedString);
}
```