Here's the patched version of the method:

```java
private MutationTestSummaryData createSummaryData(final CoverageDatabase coverage, final ClassMutationResults data) {
    byte[] classBytes = coverage.getClassBytes(data.getMutatedClass());
    long timestamp = coverage.getClassTimestamp(data.getMutatedClass());
    return new MutationTestSummaryData(data.getFileName(),
        data.getMutations(),
        ClassInfoVisitor.getClassInfo(data.getMutatedClass(), classBytes, timestamp));
}
```

This patch replaces the usage of the removed `getClassInfo` method from `CoverageDatabase` with the new `getClassInfo` method from `ClassInfoVisitor`. The method takes the class name, bytecode, and timestamp as arguments and returns the corresponding `ClassInfo` object.