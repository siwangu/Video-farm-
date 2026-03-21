import React from 'react';
import { Terminal, Github, Video, Upload, Layers, CheckCircle, AlertTriangle } from 'lucide-react';

const VideoFarmDocs = () => {
  return (
    <div className="min-h-screen bg-slate-900 text-slate-200 p-8 font-sans">
      {/* Header */}
      <header className="max-w-4xl mx-auto border-b border-slate-700 pb-8 mb-12">
        <div className="flex items-center gap-4 mb-4">
          <div className="bg-indigo-500 p-3 rounded-xl">
            <Video size={32} className="text-white" />
          </div>
          <h1 className="text-4xl font-bold tracking-tight text-white">Video Farm</h1>
        </div>
        <p className="text-xl text-slate-400">
          自动化视频生成与 YouTube 多频道分发工具。
        </p>
      </header>

      <main className="max-w-4xl mx-auto space-y-16">
        
        {/* Core Features - Grid Layout */}
        <section>
          <h2 className="text-2xl font-semibold mb-6 flex items-center gap-2 text-indigo-400">
            <Layers size={24} /> 核心特性
          </h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {[
              { title: "全自动生成", desc: "批量创建视频内容，支持 AI 流程对接。" },
              { title: "多频道轮询", desc: "支持账号自动切换，规避单一频道限制。" },
              { title: "状态追踪", desc: "实时记录上传状态与日志，便于维护。" },
              { title: "跨平台支持", desc: "兼容 Termux, Linux, 和 macOS。" },
            ].map((f, i) => (
              <div key={i} className="bg-slate-800/50 p-4 rounded-lg border border-slate-700 hover:border-indigo-500 transition-colors">
                <h3 className="font-bold text-slate-100">{f.title}</h3>
                <p className="text-sm text-slate-400">{f.desc}</p>
              </div>
            ))}
          </div>
        </section>

        {/* Project Structure - Tree View */}
        <section>
          <h2 className="text-2xl font-semibold mb-6 text-indigo-400">项目结构</h2>
          <div className="bg-slate-950 p-6 rounded-lg font-mono text-sm border border-slate-800">
            <div className="text-emerald-400">video_farm/</div>
            <div className="pl-4 border-l border-slate-700 ml-2 space-y-1 mt-2">
              <div>├── <span className="text-blue-400">farm.py</span> <span className="text-slate-500"># 主程序入口</span></div>
              <div>├── <span className="text-blue-400">upload.py</span> <span className="text-slate-500"># YouTube 模块</span></div>
              <div>├── <span className="text-amber-400">client_secret.json</span> <span className="text-slate-500"># OAuth 凭证</span></div>
              <div>├── <span className="text-emerald-400">generated_videos/</span> <span className="text-slate-500"># 视频暂存区</span></div>
              <div>└── <span className="text-slate-400 text-opacity-50">token_acc*.pickle # 授权令牌</span></div>
            </div>
          </div>
        </section>

        {/* Installation - Terminal Style */}
        <section>
          <h2 className="text-2xl font-semibold mb-6 flex items-center gap-2 text-indigo-400">
            <Terminal size={24} /> 快速开始
          </h2>
          <div className="bg-black rounded-lg overflow-hidden border border-slate-700">
            <div className="flex bg-slate-800 px-4 py-2 gap-2">
              <div className="w-3 h-3 rounded-full bg-red-500"></div>
              <div className="w-3 h-3 rounded-full bg-amber-500"></div>
              <div className="w-3 h-3 rounded-full bg-emerald-500"></div>
            </div>
            <pre className="p-6 text-indigo-300 overflow-x-auto">
              <code>{`# 安装依赖
pip install google-api-python-client google-auth-oauthlib

# 首次运行 (根据提示进行 OAuth 授权)
python3 farm.py`}</code>
            </pre>
          </div>
        </section>

        {/* Workflow Diagram Placeholder */}
        <section className="bg-indigo-900/20 border border-indigo-500/30 rounded-2xl p-8 text-center">
          <Upload className="mx-auto mb-4 text-indigo-400" size={48} />
          <h3 className="text-xl font-bold mb-2 text-white">自动化工作流</h3>
          <p className="text-slate-400 max-w-md mx-auto">
            从本地生成视频文件，自动校验 Google Token，按照配置队列轮流推送到不同的 YouTube 频道。
          </p>
        </section>

        {/* Warnings */}
        <footer className="pt-12 border-t border-slate-800">
          <div className="flex items-start gap-3 text-amber-400 bg-amber-950/30 p-4 rounded-lg">
            <AlertTriangle className="shrink-0" size={20} />
            <p className="text-sm text-amber-200/80">
              请务必遵守 YouTube API 使用政策。高频上传可能会导致 API 配额限制或频道被封禁。
            </p>
          </div>
          <div className="mt-8 text-center text-slate-500 text-sm italic">
            Licensed under MIT License • Open source for automation
          </div>
        </footer>
      </main>
    </div>
  );
};

export default VideoFarmDocs;
