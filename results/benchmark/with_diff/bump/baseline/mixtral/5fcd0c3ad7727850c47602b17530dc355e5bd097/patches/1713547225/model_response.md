Here's the proposed patch for the failing method:

```java
private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassName mutatedClass = data.getMutatedClass();
    byte[] classFile = coverage.getClassFile(mutatedClass);
    long timestamp = coverage.getClassTime(mutatedClass);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(), ClassInfoBuilder.getClassInfo(mutatedClass, classFile, timestamp));
}
```

This patch uses the new `getClassInfo` method from `ClassInfoVisitor` to create a `ClassInfo` object. It first retrieves the class file and timestamp from the `CoverageDatabase` and then uses these values to create the `ClassInfo` object.