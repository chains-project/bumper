```java
  private Matcher<String> manifestPushed() {
        return new StringContains(this.image.digest());
    }
```