```java
private Matcher<String> manifestPushed() {
    return new StringContains(String.format("latest: digest: %s", this.image.digest()));
}
```