```java
@Override
private Matcher<String> layersPushed() {
    // Create a matcher that checks if the string contains the specified substring, ignoring case.
    final Matcher<String> matcher = new StringContains(false, this.image.layer());
    // Return the matcher.
    return matcher;
}
```