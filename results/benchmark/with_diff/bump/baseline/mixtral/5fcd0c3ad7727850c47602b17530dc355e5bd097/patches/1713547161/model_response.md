Here is a possible patch for the failing code:

```java
private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    Collection<ClassInfo> classInfo = new ArrayList<>();
    for (ClassName className : data.getMutatedClass()) {
        byte[] classBytes = coverage.getRawClass bytes(className);
        long timestamp = coverage.getTimestamp(className);
        classInfo.add(ClassInfoBuilder.forClass(className, classBytes, timestamp));
    }
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```

This patch uses the new `ClassInfoBuilder` method to create `ClassInfo` objects from the raw class bytes and timestamp, which can be obtained from the `CoverageDatabase`. The resulting `ClassInfo` objects are added to a list, which is then passed to the `MutationTestSummaryData` constructor. This should fix the error caused by the removed `getClassInfo` method.