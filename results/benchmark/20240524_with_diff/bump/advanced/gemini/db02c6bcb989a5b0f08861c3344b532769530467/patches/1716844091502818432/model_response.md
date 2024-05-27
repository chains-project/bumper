```java
private org.hamcrest.Matcher<java.lang.String> manifestPushed() {
    return org.hamcrest.Matchers.stringContainsInOrder(false, java.lang.String.format("latest: digest: %s", this.image.digest()));
}
```