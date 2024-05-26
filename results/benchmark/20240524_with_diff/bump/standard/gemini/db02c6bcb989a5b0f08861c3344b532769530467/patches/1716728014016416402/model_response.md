```java
private org.hamcrest.Matcher<java.lang.String> manifestPushed() {
    return new org.hamcrest.core.StringContains(false, this.image.digest().toString());
}
```