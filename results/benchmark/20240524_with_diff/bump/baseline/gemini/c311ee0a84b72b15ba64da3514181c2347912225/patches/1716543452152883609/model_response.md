```java
private Matcher<String> manifestPushed() {
    String imageDigest = this.image.digest();
    String expectedString = String.format("latest: digest: %s", imageDigest);
    return new StringContains(false, expectedString);
}
```