```java
private Matcher<String> manifestPushed() {
    return CoreMatchers.containsString(String.format("latest: digest: %s", this.image.digest()));
}
```