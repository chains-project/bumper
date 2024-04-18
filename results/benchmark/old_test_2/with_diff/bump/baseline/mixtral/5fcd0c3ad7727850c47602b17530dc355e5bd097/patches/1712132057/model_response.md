Based on the error message and the library changes, it seems that the `getClassInfo` method of `CoverageDatabase` is no longer available in the new library version. Instead, a new `getClassInfo` method is added to `ClassInfoVisitor`. Here's a possible patch for the failing code:

```java
private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    ClassInfo classInfo = ClassInfo.forName(data.getMutatedClass());
    byte[] classBytes = coverage.getRawClassContent(classInfo);
    long timestamp = coverage.getTimestamp(classInfo);
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(),
        ClassInfoVisitor.getClassInfo(classInfo, classBytes, timestamp));
}
```

In this patch, we first get the `ClassInfo` object for the mutated class using the `forName` method of `ClassInfo`. Then, we get the raw class content and timestamp from the `CoverageDatabase` using the `getRawClassContent` and `getTimestamp` methods. Finally, we use the new `getClassInfo` method of `ClassInfoVisitor` to get the `ClassInfoBuilder` for the class, and create a `MutationTestSummaryData` object using it.