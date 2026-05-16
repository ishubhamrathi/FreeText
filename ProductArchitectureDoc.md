# FreeText — Product Architecture Document

## Overview

**FreeText** is a privacy-first local AI dictation assistant for Windows.

The application runs natively on Windows and allows users to:

* speak naturally
* automatically transcribe speech
* clean and structure the text using AI
* type directly into any active application

Unlike traditional speech-to-text tools, FreeText focuses on:

* intelligent transcription cleanup
* local/offline processing
* contextual formatting
* low-latency typing workflows

The product is designed for developers, professionals, writers, and power users who type frequently and want a faster, more natural interaction model with their computer.

---

# Core Problem

Existing speech-to-text tools often:

* produce messy transcripts
* include filler words
* require cloud processing
* lack contextual formatting
* feel slow or inaccurate
* do not integrate deeply into desktop workflows

Users still spend time:

* correcting grammar
* fixing punctuation
* reformatting sentences
* manually copying text

FreeText solves this by adding an AI post-processing layer between speech recognition and typing output.

---

# Product Goals

## Primary Goals

* Real-time voice typing
* Offline/local-first processing
* Intelligent transcript cleanup
* Native Windows integration
* Minimal latency
* Works across all applications

## Secondary Goals

* Context-aware writing modes
* Voice commands
* AI rewriting
* App-specific behavior
* Privacy-first architecture

---

# High-Level Architecture

```text
┌───────────────────────────┐
│   Windows Native Client   │
│  (Tauri + React Frontend) │
└─────────────┬─────────────┘
              │ IPC
              ▼
┌───────────────────────────┐
│     Python AI Service     │
├───────────────────────────┤
│ Wake Word Detection       │
│ Audio Streaming           │
│ Voice Activity Detection  │
│ Speech-to-Text Engine     │
│ AI Text Cleanup           │
│ Command Processing        │
└─────────────┬─────────────┘
              ▼
┌───────────────────────────┐
│ Windows Input Simulator   │
│ (Keyboard Typing Engine)  │
└─────────────┬─────────────┘
              ▼
       Active Application
```

---

# Technology Stack

| Layer               | Technology               |
| ------------------- | ------------------------ |
| Desktop Framework   | Tauri                    |
| Frontend UI         | React + TypeScript       |
| Backend AI Engine   | Python                   |
| Speech Recognition  | faster-whisper           |
| Local LLM Runtime   | Ollama                   |
| Wake Word Detection | Porcupine / openWakeWord |
| Database            | SQLite                   |
| Native Typing       | Win32 APIs               |
| Packaging           | Tauri Installer          |

---

# System Components

---

# 1. Desktop Application Layer

## Responsibilities

* UI rendering
* settings management
* onboarding
* system tray integration
* hotkey configuration
* microphone controls

## Technology

* Tauri
* React
* TypeScript

## Why Tauri

* lightweight memory usage
* native Windows support
* secure architecture
* small installer size
* Rust backend integration

---

# 2. Audio Capture Service

## Responsibilities

* microphone access
* streaming audio capture
* buffering
* noise suppression
* audio chunk processing

## Pipeline

```text
Microphone
   ↓
Audio Buffer
   ↓
Voice Activity Detection
   ↓
Speech Processor
```

## Considerations

* low latency
* background execution
* efficient CPU usage

---

# 3. Wake Word Detection

## Example Wake Words

* “Nova”
* “Atlas”
* “Computer”

## Responsibilities

* passive listening
* trigger speech recording
* reduce accidental activation

## Recommended Engine

* Porcupine
* openWakeWord

---

# 4. Speech-to-Text Engine

## Responsibilities

* convert speech into text
* streaming transcription
* punctuation prediction
* multi-language support

## Recommended Engine

* faster-whisper

## Why faster-whisper

* offline support
* GPU acceleration
* high transcription accuracy
* fast inference
* production-ready ecosystem

---

# 5. AI Cleanup Layer

This is the core differentiator of the product.

## Input Example

```text
uhh hey can you like send the report tomorrow morning
```

## Output Example

```text
Hey, can you send the report tomorrow morning?
```

## Responsibilities

* grammar correction
* punctuation restoration
* filler word removal
* sentence restructuring
* tone adjustment
* formatting improvements

## Recommended Runtime

* Ollama

## Suggested Models

| Model       | Usage                    |
| ----------- | ------------------------ |
| Phi-3 Mini  | lightweight fast cleanup |
| Gemma 3 4B  | balanced performance     |
| Qwen 2.5 3B | high-quality formatting  |

---

# 6. Command Processing Engine

## Example Commands

```text
"email mode"
"professional mode"
"rewrite professionally"
"start coding mode"
```

## Responsibilities

* detect command intent
* switch formatting modes
* execute desktop actions
* trigger workflows

---

# 7. Native Typing Engine

## Responsibilities

* detect active window
* simulate keyboard typing
* inject processed text
* preserve cursor position

## Windows APIs

* SendInput API
* Win32 Keyboard Hooks

## Alternatives

* pynput
* pyautogui

Production builds should prefer native Win32 integration for reliability.

---

# 8. Local Database

## Recommended Database

* SQLite

## Stored Data

* user settings
* hotkeys
* custom commands
* prompt presets
* wake words
* usage logs

No cloud dependency required.

---

# Processing Workflow

```text
1. User speaks wake word
2. App activates recording
3. Audio stream is buffered
4. Voice activity detection filters silence
5. Speech converted to raw transcript
6. AI cleanup engine processes transcript
7. Final text sent to typing engine
8. Text typed into active application
```

---

# Example User Flow

## Scenario

User is chatting in Slack.

### User Says

```text
Nova send message to Rahul saying I will join in ten minutes
```

### Internal Pipeline

```text
Wake Word Detection
   ↓
Speech Recognition
   ↓
Transcript Cleanup
   ↓
Command Detection
   ↓
Typing Injection
```

### Final Typed Output

```text
I’ll join in 10 minutes.
```

---

# Key Features

---

# Feature 1 — Push-to-Talk Mode

## Hotkey

```text
Ctrl + Shift + Space
```

## Benefits

* reduces accidental triggers
* lower CPU usage
* better privacy

---

# Feature 2 — Smart Formatting Modes

## Modes

| Mode         | Behavior                  |
| ------------ | ------------------------- |
| Casual       | conversational tone       |
| Professional | polished grammar          |
| Coding       | minimal punctuation       |
| Email        | structured formal writing |

---

# Feature 3 — App-Aware Formatting

The application detects active software and adjusts formatting automatically.

## Examples

| Application | Formatting   |
| ----------- | ------------ |
| Slack       | casual       |
| Gmail       | professional |
| VSCode      | coding mode  |

---

# Feature 4 — Offline Privacy Mode

All processing occurs locally.

No:

* cloud uploads
* external API dependency
* remote transcript storage

This becomes a major product differentiator.

---

# Non-Functional Requirements

| Requirement     | Goal                               |
| --------------- | ---------------------------------- |
| Startup Time    | < 3 seconds                        |
| Typing Delay    | < 500ms                            |
| Offline Support | Full                               |
| RAM Usage       | < 500MB idle                       |
| CPU Usage       | Optimized for background execution |

---

# Security & Privacy

## Principles

* local-first architecture
* encrypted settings storage
* no mandatory cloud sync
* optional telemetry only
* microphone access transparency

---

# Packaging & Distribution

## Installer

* Windows MSI / EXE installer
* auto-start option
* system tray integration

## Auto Updates

Potential future integration:

* Tauri updater
* GitHub Releases

---

# MVP Scope

## Phase 1

* push-to-talk
* speech transcription
* AI cleanup
* typing injection

## Phase 2

* wake word support
* streaming transcription
* smart formatting modes

## Phase 3

* app-aware formatting
* contextual AI rewriting
* command workflows
* plugin ecosystem

---

# Resume Value

This project demonstrates:

* desktop systems engineering
* AI integration
* local inference pipelines
* real-time audio processing
* OS-level integrations
* product architecture design
* performance optimization
* privacy-first AI systems

This is significantly stronger than standard CRUD or chatbot projects because it combines AI with systems-level engineering and real user workflows.
