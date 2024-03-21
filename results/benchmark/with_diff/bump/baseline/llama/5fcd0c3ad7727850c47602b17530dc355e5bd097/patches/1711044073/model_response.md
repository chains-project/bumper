Here's a proposed patch to fix the error:
```java
private MutationTestSummaryData createSummaryData(
    final CoverageDatabase coverage, final ClassMutationResults data) {
    // Create a new ClassInfoBuilder with the class name and bytecode
    org.pitest.classinfo.ClassInfoBuilder classInfoBuilder = new org.pitest.classinfo.ClassInfoBuilder(data.getMutatedClass().getName(), data.getMutatedClass().getBytes());
    // Get the ClassInfo object using the ClassInfoBuilder
    org.pitest.classinfo.ClassInfo classInfo = classInfoBuilder.build();
    // Create a new MutationTestSummaryData using the ClassInfo object
    return new MutationTestSummaryData(data.getFileName(), data.getMutations(), classInfo);
}
```
The patch creates a new `ClassInfoBuilder` with the class name and bytecode, then uses it to build a `ClassInfo` object. The `ClassInfo` object is then passed to the `MutationTestSummaryData` constructor, along with the file name and mutations, to create a new `MutationTestSummaryData` object.

This patch uses the `org.pitest.classinfo.ClassInfoBuilder` class, which is a new addition in the updated library version, to create a `ClassInfo` object. This eliminates the need to use the removed `getClassInfo` method.