# Architecture

AutoVideo Studio follows a pipeline architecture:

1. **Input**
   - title
   - script
   - speaking speed

2. **Scene planner**
   - normalizes the script;
   - splits it into scenes;
   - estimates scene duration.

3. **Subtitle generator**
   - converts scene timestamps to SRT.

4. **Project model**
   - stores the complete render plan.

5. **Renderer**
   - converts the render plan into an MP4 using FFmpeg.

Future modules can attach AI scene planning, TTS, image generation,
stock-media retrieval and template systems without changing the core pipeline.
