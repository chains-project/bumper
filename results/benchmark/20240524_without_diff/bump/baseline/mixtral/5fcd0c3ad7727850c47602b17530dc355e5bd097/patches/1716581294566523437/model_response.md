Here's the proposed patch for the given failing client code:

```java
private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfo classInfo = coverage.getClassInfo(Collections.singleton(data.getMutatedClass()));
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```

This patch should resolve the error by storing the `ClassInfo` object in a separate variable before returning the `MutationTestSummaryData` object. This makes the code easier to understand and helps avoid any potential issues with method chaining or order of operations.